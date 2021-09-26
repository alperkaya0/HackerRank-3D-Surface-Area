# HackerRank-3D-Surface-Area
I want to add my comment at discussion tab:

"""

This question looks really hard at first but when you realise that you need to think from bottom to up, it gets really easy.Let me tell you about my solution and give code of it.

![](https://prnt.sc/1tpx631)

At first let's just build our toy from bottom to up and let's consent surface area of each block as 6.
And you can see that I omit 1 from every cell if it's not 0, basically i am spending my blocks to build 3d toy.

What now ? We will omit the adjacent surfaces and we will do it in 3 parts!
First adjacent rows at the same layer(area -= 2 if both adjacent(horizantally) cell bigger than 0(not empty)).
2-Adjacent columns at the same layer.
3-Adjacent tops between layers.

	
"""
