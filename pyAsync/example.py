import asyncio
import random


async def get_random_till_thresh(thresh):
    try:
        if thresh > 10:
            print("Not allowed")
            raise NotImplementedError
        ii = random.randint(1, 10)

        while (ii <= thresh):
            print("Generating random number once more...")
            ii = random.randint(1, 10)
            await asyncio.sleep(1)
        await asyncio.sleep(1)
        return ii
    except NotImplementedError as e:
        return -1


async def main():
    # res = await asyncio.gather(*(get_random_till_thresh(i) for i in [12, 3, 5]))
    # this is similar to

    res = await asyncio.gather(get_random_till_thresh(6),
                               get_random_till_thresh(7),
                               get_random_till_thresh(8))
    return res


r1, r2, r3 = asyncio.run(main())

print(r1, r2, r3)
