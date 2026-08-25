focal_length_available= [
    4, 5.6, 6, 7.5, 8, 9, 10, 11, 12, 14, 15, 16, 18, 20, 21, 24, 25, 28, 30, 32, 35, 40, 42.5, 45, 50, 55, 58, 60, 65, 75, 85, 90, 100, 105, 135, 180, 200, 300, 400, 500, 600, 800, 1200
    ]

focal_aperture_available = [
    0.7, 0.95, 1.0, 1.2, 1.4, 1.8, 2.0, 2.5, 2.8, 3.2, 3.5, 4.0, 4.5, 5.0, 5.6, 6.3, 7.1, 8.0, 9.0, 10.0, 11.0, 13.0, 14.0, 16.0, 18.0, 20.0, 22.0, 32.0
    ]

crop_factor = {
    "full_frame":1.0,
    "apsc":1.5,
    "apsc_canon":1.6,
    "mft": 2.0,
    "one_inch":2.73
}

crop_adapters = {
    1: ("None", 1.0),
    2: ("Speedbuster (0.71x)", 0.71),
    3: ("Speedbuster (0.64x)", 0.64),
    4: ("Tele converter (1.4x)", 1.4),
    5: ("Tele converter (2x)", 2.0)
}

greetings = [
    "Goodmorning",
    "Hi",
    "Welcome",
    "Hey there!",
    "Welcome back",
    "Hey",
    "Hola"
]

length_classification = [
    (0, 12, "fisheye"),
    (12.01, 35, "wide-angle"),
    (35.011, 50, "normal"),
    (50.01, 80, "short telephoto"),
    (80.01, 200, "telephoto lens"),
    (200.01, 6553, "super-telephoto")
]

aperture_classification = [
    (0, 2.2, 5),
    (2.21, 3.5, 4),
    (3.51, 5, 3),
    (5.01, 7, 2),
    (7.01, 179, 1)
]

