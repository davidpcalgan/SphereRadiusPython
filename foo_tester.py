import sphere_volume

#simple sanity checks
print(sphere_volume.foo(1))
print(sphere_volume.foo(10))
print(sphere_volume.foo(4.3))

#testing value validation
try:
    print(sphere_volume.foo(-2))
except ValueError:
    print("Radius must be a non-negative number.")

