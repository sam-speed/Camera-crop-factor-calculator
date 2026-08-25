from data import crop_factor, crop_adapters, length_classification, aperture_classification

def apply_crop(sensor_name, value):
    crop_factor_value = crop_factor[sensor_name]
    return round(value * crop_factor_value, 1)

def apply_adapter(adapter_choice, value):
    adapter_multiplier = crop_adapters[adapter_choice][1]
    return round(value * adapter_multiplier, 1)

def classify_focal_length(focal_length):
    for minimum, maximum, name in length_classification:
        if minimum <= focal_length <= maximum:
            return name
    return "Unknown"

def aperture_ranking(aperture):
    for minimum, maximum, ranking in aperture_classification:
        if minimum <= aperture <= maximum:
            return ranking
    return "Unknown"
    