import asyncio


async def add_number(num1, num2):
    await asyncio.sleep(num1)
    print(f"slept for {num1}")
    return num1 + num2


async def main():
    res = await asyncio.gather(*(add_number(i, i) for i in range(1, 11)))
    return res

res = asyncio.run(main())

print(res)
