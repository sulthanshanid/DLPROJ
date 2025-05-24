
            
import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

def preprocess_green_captcha(image_path):
    """Optimized preprocessing for green text CAPTCHAs"""
    # Read image
    image = cv2.imread(image_path)
    if image is None:
        # Try with PIL if cv2 fails
        pil_image = Image.open(image_path)
        image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    
    # Extract green channel for green text
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define range for green color
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    
    # Create mask for green text
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    processed_images = []
    method_names = []
    
    # Method 1: Green channel extraction with inversion
    green_extracted = cv2.bitwise_not(green_mask)
    processed_images.append(green_extracted)
    method_names.append("Green Channel Extraction")
    
    # Method 2: Enhanced contrast
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)
    _, enhanced_thresh = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    processed_images.append(enhanced_thresh)
    method_names.append("Enhanced Contrast")
    
    # Method 3: Inverted threshold
    _, inv_thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    processed_images.append(inv_thresh)
    method_names.append("Inverted Threshold")
    
    # Method 4: Adaptive threshold
    adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                    cv2.THRESH_BINARY_INV, 15, 10)
    processed_images.append(adaptive)
    method_names.append("Adaptive Threshold")
    
    # Method 5: Bilateral filter
    bilateral = cv2.bilateralFilter(gray, 9, 75, 75)
    _, bilateral_thresh = cv2.threshold(bilateral, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    processed_images.append(bilateral_thresh)
    method_names.append("Bilateral Filter")
    
    return processed_images, method_names, image

def solve_with_multiple_configs(processed_images, method_names):
    """Try multiple OCR configurations"""
    configs = [
        ('PSM 8 + Whitelist', '--psm 8 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'),
        ('PSM 7 + Whitelist', '--psm 7 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'),
        ('PSM 6 + Whitelist', '--psm 6 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'),
        ('PSM 8 Default', '--psm 8'),
        ('PSM 7 Default', '--psm 7'),
    ]
    
    all_results = []
    
    for i, (processed_img, method_name) in enumerate(zip(processed_images, method_names)):
        for config_name, config in configs:
            try:
                # Convert to PIL and scale up
                pil_img = Image.fromarray(processed_img)
                width, height = pil_img.size
                pil_img = pil_img.resize((width * 2, height * 2), Image.Resampling.LANCZOS)
                
                text = pytesseract.image_to_string(pil_img, config=config).strip()
                clean_text = ''.join(c for c in text if c.isalnum())
                
                if clean_text and 4 <= len(clean_text) <= 8:
                    confidence = len(clean_text)
                    if len(clean_text) == 6:
                        confidence += 5
                    if any(c.isupper() for c in clean_text) and any(c.islower() for c in clean_text):
                        confidence += 3
                    if any(c.isalpha() for c in clean_text) and any(c.isdigit() for c in clean_text):
                        confidence += 2
                    
                    all_results.append({
                        'text': clean_text,
                        'confidence': confidence,
                        'method': method_name,
                        'config': config_name,
                        'method_index': i
                    })
            except Exception as e:
                continue
    
    return all_results

def visualize_processing(original_image, processed_images, method_names, results, image_name):
    """Visualize the processing steps and results"""
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle(f'CAPTCHA Processing: {image_name}', fontsize=16)
    
    # Show original
    axes[0, 0].imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title('Original Image')
    axes[0, 0].axis('off')
    
    # Show processed images
    for i, (img, name) in enumerate(zip(processed_images[:5], method_names[:5])):
        row = (i + 1) // 3
        col = (i + 1) % 3
        axes[row, col].imshow(img, cmap='gray')
        axes[row, col].set_title(name)
        axes[row, col].axis('off')
    
    plt.tight_layout()
    
    # Print results
    print(f"\n=== Results for {image_name} ===")
    if results:
        best_result = max(results, key=lambda x: x['confidence'])
        print(f"BEST RESULT: {best_result['text']}")
        print(f"Method: {best_result['method']}")
        print(f"Config: {best_result['config']}")
        print(f"Confidence: {best_result['confidence']}")
        
        print(f"\nAll candidates (top 10):")
        sorted_results = sorted(results, key=lambda x: x['confidence'], reverse=True)[:10]
        for result in sorted_results:
            print(f"  {result['text']} | {result['method']} | {result['config']} | Conf: {result['confidence']}")
    else:
        print("No valid results found")
    
    plt.show()
    return results[0]['text'] if results else "Failed"

def test_captcha_images():
    """Test the CAPTCHA solver on your sample images"""
    # Test images - replace with your actual image paths
    test_images = [
        ("captcha1.png", "4MTe9z"),  # Expected result
        ("captcha2.png", "mqhzp4"),  # Expected result  
        ("captcha3.png", "qKVnZc"),  # Expected result
    ]
    
    results_summary = []
    
    for image_path, expected in test_images:
        try:
            print(f"\n{'='*50}")
            print(f"Processing: {image_path}")
            print(f"Expected: {expected}")
            
            # Process image
            processed_images, method_names, original = preprocess_green_captcha(image_path)
            
            # Solve with multiple methods
            results = solve_with_multiple_configs(processed_images, method_names)
            
            # Visualize and get best result
            best_result = visualize_processing(original, processed_images, method_names, results, image_path)
            
            # Check accuracy
            is_correct = best_result.lower() == expected.lower()
            results_summary.append({
                'image': image_path,
                'expected': expected,
                'result': best_result,
                'correct': is_correct
            })
            
            print(f"Result: {best_result}")
            print(f"Correct: {'✓' if is_correct else '✗'}")
            
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            results_summary.append({
                'image': image_path,
                'expected': expected,
                'result': f"Error: {e}",
                'correct': False
            })
    
    # Final summary
    print(f"\n{'='*50}")
    print("FINAL SUMMARY")
    print(f"{'='*50}")
    
    correct_count = sum(1 for r in results_summary if r['correct'])
    total_count = len(results_summary)
    accuracy = (correct_count / total_count * 100) if total_count > 0 else 0
    
    for result in results_summary:
        status = "✓" if result['correct'] else "✗"
        print(f"{status} {result['image']}: {result['expected']} -> {result['result']}")
    
    print(f"\nAccuracy: {correct_count}/{total_count} ({accuracy:.1f}%)")

if __name__ == "__main__":
    # Test the solver
    test_captcha_images()
    
    print("\nTo use with your GUI application:")
    print("1. Save your CAPTCHA images as captcha1.png, captcha2.png, captcha3.png")
    print("2. Run this script to test accuracy")
    print("3. Use the main GUI application with your CAPTCHA URL")