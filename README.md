# surfs_up
---
## Overview of the Analysis

For this analysis, temperature data for the months of June and December was investigated to find temperature trends. Using this data, a decison could be made on whether or not to open an ice cream shop/surf shop during these months. The goal was to make a profitable business year-round, so determining the right location and weather was crucial in order to make that happen.

The technology used throughout this analysis was a SQLite database, VS Code, and Flask. SQLAlchemy and its extensions were used to create a connection engine and was faster to use since it is a smaller database than using a larger one like pgAdmin. VS Code assisted with enabling the connection with Flask, which made creating an app route to the web possible.

---

## Analysis Results

The image below shows the code used to retrieve the statistical values needed to perform the analysis of temperature for the month of June.

![June_temp_stats](https://github.com/YolandaCasica/surfs_up/blob/master/Images/June_temp_stats.png)

The code block was refactored slightly to determine the data for December.

![Dec_temp_stats](https://github.com/YolandaCasica/surfs_up/blob/master/Images/Dec_temp_stats.png)

What could be analyzed for both of these months:

* At a first glance, the minimum temperatures for both months was predictably lower during that time of year, December being the lowest.
* The maximum temperature for both had an even less gap with only a two degree difference, December still being the lowest degrees.
* The average temperatures for both months was actually very close. June had an average of 74 degrees and December had an average of 71 degrees. 

---

## Summary 

As the coding and images analysis shows above, an ice cream business could still have a chance of making a a decent profit margin during these two months. Since the average  temperature for both is so close, there is not much unpredicatable weather deviation. The weather is definitely cooler during these months, however, it would not go to a freezing point, so customers could still be expected to make ice cream purchases. There may be some profit less on the surf side of the shop since not many people would be surfing during the coldest month of the year. A survey could be given out to that area to see how many people still enjoy eating ice cream during cooler months. 

The code could be refactored again to show the months after December to see how fast the weather stays at a 70 degree average temp. 
