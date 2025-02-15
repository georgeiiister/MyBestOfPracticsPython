while True:
    try:
        nums = tuple((int(input(f'input number {i+1} >> ')) for i in range(3)))
    except ValueError:
        print(f'you input not number!')
        continue
    print('min:', min(nums))
    break