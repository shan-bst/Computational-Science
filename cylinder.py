from decimal import Decimal, getcontext

# set precision for 100+ digits
getcontext().prec = 120

# pi reference string
pi = Decimal(
    "3.14159265358979323846264338327950288419716939937510"
    "58209749445923078164062862089986280348253421170679"
)

# cylinder variables
radius = Decimal("2")
height = Decimal("10")
constant_factor = (radius**2) * height

# baseline volume
real_volume = pi * constant_factor

# truncation logic
def truncate(value, decimals):
    factor = Decimal(10) ** decimals
    return (value * factor // 1) / factor

# precision level
precision_levels = [20, 40, 60, 100]

print("--- CYLINDER VOLUME ERROR ANALYSIS ---")
print(f"True Volume Reference: {real_volume}\n")

# loop through precision stages
for p in precision_levels:
    # get pi versions
    pi_t = truncate(pi, p)
    pi_r = pi.quantize(Decimal(f"1e-{p}"))

    # calculate volumes
    vol_t = pi_t * constant_factor
    vol_r = pi_r * constant_factor

    print(f"========================================")
    print(f"PRECISION STAGE: {p} DECIMAL PLACES")
    print(f"========================================")
    
    print(f"Truncated pi = {pi_t:f}")
    print(f"Volume (Truncation) = {vol_t:f}")
    print(f"Rounded pi = {pi_r:f}")
    print(f"Volume (Rounding) = {vol_r:f}")
    
    # calculate gap
    diff = abs(vol_r - vol_t)
    print(f"Difference = {diff:E}")
    print()