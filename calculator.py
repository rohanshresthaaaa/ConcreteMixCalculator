def wet_volume(length, width, depth):
    return length * width * depth

def dry_volume(wet_vol):
    return wet_vol * 1.54

def material_quantities(dry_vol, c, s, a):
    total = c + s + a
    cement = (c / total) * dry_vol
    sand = (s / total) * dry_vol
    aggregate = (a / total) * dry_vol
    return cement, sand, aggregate

def cement_bags(cement_volume):
    return cement_volume / 0.0347

def water_required(cement_volume, wc_ratio):
    cement_mass = cement_volume * 1440
    return cement_mass * wc_ratio

wet = wet_volume(4, 3, 0.15)
dry = dry_volume(wet)

cement, sand, aggregate = material_quantities(dry, 1, 2, 4)
bags = cement_bags(cement)
water = water_required(cement, 0.5)

print(f"Wet Volume: {wet:.3f} m^3")
print(f"Dry Volume: {dry:.3f} m^3")
print(f"Cement Volume: {cement:.3f} m^3")
print(f"Sand Volume: {sand:.3f} m^3")
print(f"Aggregate Volume: {aggregate:.3f} m^3")
print(f"Cement Bags: {bags:.2f}")
print(f"Water Required: {water:.2f} liters")