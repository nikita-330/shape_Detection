import cv2
import numpy as np
import random

def generate_random_shape(image_size):
    image = np.ones((image_size, image_size, 3), dtype=np.uint8) * 255
    shape_type = random.choice(['circle', 'line', 'ellipse', 'rectangle', 'rounded_rectangle', 'polygon', 'star', 'basketball'])
    
    if shape_type == 'circle':
        center = (random.randint(50, image_size-50), random.randint(50, image_size-50))
        radius = random.randint(20, 50)
        cv2.circle(image, center, radius, (0, 0, 0), -1)
    elif shape_type == 'line':
        pt1 = (random.randint(0, image_size), random.randint(0, image_size))
        pt2 = (random.randint(0, image_size), random.randint(0, image_size))
        cv2.line(image, pt1, pt2, (0, 0, 0), 2)
    elif shape_type == 'ellipse':
        center = (random.randint(50, image_size-50), random.randint(50, image_size-50))
        axes = (random.randint(20, 50), random.randint(20, 50))
        angle = random.randint(0, 360)
        cv2.ellipse(image, center, axes, angle, 0, 360, (0, 0, 0), -1)
    elif shape_type == 'rectangle':
        pt1 = (random.randint(0, image_size-50), random.randint(0, image_size-50))
        pt2 = (pt1[0] + random.randint(20, 50), pt1[1] + random.randint(20, 50))
        cv2.rectangle(image, pt1, pt2, (0, 0, 0), -1)
    elif shape_type == 'rounded_rectangle':
        pt1 = (random.randint(0, image_size-50), random.randint(0, image_size-50))
        pt2 = (pt1[0] + random.randint(20, 50), pt1[1] + random.randint(20, 50))
        radius = 10
        cv2.rectangle(image, pt1, pt2, (0, 0, 0), -1)
        cv2.circle(image, pt1, radius, (255, 255, 255), -1)
        cv2.circle(image, (pt2[0], pt1[1]), radius, (255, 255, 255), -1)
        cv2.circle(image, (pt2[0], pt2[1]), radius, (255, 255, 255), -1)
        cv2.circle(image, (pt1[0], pt2[1]), radius, (255, 255, 255), -1)
    elif shape_type == 'polygon':
        num_sides = random.randint(3, 8)
        points = []
        for _ in range(num_sides):
            points.append([random.randint(50, image_size-50), random.randint(50, image_size-50)])
        points = np.array(points, np.int32).reshape((-1, 1, 2))
        cv2.polylines(image, [points], isClosed=True, color=(0, 0, 0), thickness=2)
        cv2.fillPoly(image, [points], color=(0, 0, 0))
    elif shape_type == 'star':
        num_points = random.randint(5, 8) * 2
        radius_outer = random.randint(30, 50)
        radius_inner = radius_outer // 2
        center = (random.randint(50, image_size-50), random.randint(50, image_size-50))
        points = []
        angle = np.pi / num_points
        for i in range(num_points):
            r = radius_outer if i % 2 == 0 else radius_inner
            x = center[0] + int(r * np.cos(i * angle))
            y = center[1] + int(r * np.sin(i * angle))
            points.append([x, y])
        points = np.array(points, np.int32).reshape((-1, 1, 2))
        cv2.polylines(image, [points], isClosed=True, color=(0, 0, 0), thickness=2)
        cv2.fillPoly(image, [points], color=(0, 0, 0))
    elif shape_type == 'basketball':
        center = (random.randint(50, image_size-50), random.randint(50, image_size-50))
        radius = random.randint(20, 50)
        cv2.circle(image, center, radius, (0, 0, 0), 2)
        cv2.line(image, (center[0] - radius, center[1]), (center[0] + radius, center[1]), (0, 0, 0), 2)
        cv2.line(image, (center[0], center[1] - radius), (center[0], center[1] + radius), (0, 0, 0), 2)
        cv2.ellipse(image, center, (radius, radius//2), 0, 0, 360, (0, 0, 0), 2)
        cv2.ellipse(image, center, (radius//2, radius), 0, 0, 360, (0, 0, 0), 2)
    
    return image