<snippet>
  <content>
# Agile TweetViz - Team Technocrats

AgileTweetViz provides an intuitive way of representing twitter feeds. It uses different visualization techniques to present information obtained from analysis of large amount of twitter feeds. This system uses Moose Platform - build upon Pharo - to house all the feeds in a custom designed model. A separate visualization component leverage Roassal's visualization engine. This component is assisted by a FeedParser unit that helps it to scrape through the model, mine data  and use this aggregated information for its visualization unit. Additionally this project implements a sentiment analyzer in the backend which can be used for opinion mining.

## Project Website
https://sites.google.com/a/asu.edu/technocrats/


## Installation

1. Install Python v2.7

2. Moose:
Download Moose 5.1 from http://www.moosetechnology.org (install based on the operating system). The package contains Pharo, Roassal and Nautilus browser. Unzip the package in any of your directories. Launch Pharo by double clicking Pharo.exe. This usage is same for all operating systems.

3. NeoJSON:
The NeoJSON library contains NeoJSONReader which parses JSON to Pharo object. Similarly, NeoJSONWritter generates JSON from Pharo object. Go to Playground and run following commands for using NeoJSON.
```
Gofer new
  smalltalkhubUser: '' project: 'VincentBlondeau/MooseOnWeb';
  package: 'ConfigurationOfMooseOnWeb';
  load.

Gofer new
  smalltalkhubUser: 'SvenVanCaekenberghe' project: 'Neo';
  package: 'ConfigurationOfNeoCSV';
  load.
```

## Usage
1. Open Moose IDE

2. Open Playground and run the following commands to see the GUI:
```
t := TotalTweets new.

// To see visualizations with 1D - data
t showTweetVizStats.

// To see visualizations with 2D - data
t showTweetVizRelational.

// To see visualizations with 3D - data
t showTweetVizNextGen.

```


## Contributing

Pull code from github into the Moose IDE. (Refer the Change Management Process on the project website for more details on this).

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-visualization`
3. Commit your changes: `git commit -am 'Added some visualization'`
4. Push to the branch: `git push origin my-new-visualization`
5. Submit a pull request :D

## Authors

Aditya Bivalkar

Meenal Kulkarni

Tanmay Patil

Kedar Pitke

Snehal Shendware


</content>
</snippet>
