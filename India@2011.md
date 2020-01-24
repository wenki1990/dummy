<h1><center>INDIA Census 2011</center></h1>
<center><a href="https://youtu.be/SdT4mogSeOk" target="_blank">Demo Video on Youtube</a></center>

<center><a href="https://public.tableau.com/profile/satya.venkatesh#!/vizhome/India2011_15779645968680/Dashboard1" target="_blank">Tableau Public Link</a></center>

<center><img src="images/1.png" width = 600 height = 350></center>





<center><img src="images/2.png" width = 600 height = 350>


<center><img src="images/3.png" width = 600 height = 350></center>

<center><img src="images/4.png" width = 600 height = 350></center>

<center><img src="images/5.png" width = 600 height = 350></center>

<a href="https://youtu.be/SdT4mogSeOk" target="_blank">Demo Video on Youtube</a>

<a href="https://public.tableau.com/profile/satya.venkatesh#!/vizhome/India2011_15779645968680/Dashboard1" target="_blank">Tableau Public Link</a>

<h4> Concepts Used </h4>

- Maps
- Resolving Unknown values for plotting on the map
- Parameters
- Calculated Fields with Parameter
- Filters
- Highlight and Hyperlink Dashboard Actions
- Measure values and Measure name

<h4> About the Data Set </h4>

<h4> Challenges with the Data Set </h4>

- First issue was this data dates back to 2011 when there was no Telangana. I had to change the state name of the districts that are presently in Telangana. To do this, I created a calculated field with an "if condition" in it. If the district name is equal to the district name that is presently in Telangana(which I got from Wikipedia), then change the state name to Telangana.

- Next issue was plotting districts on the Indian map. Some of the Districts were not getting captured because  there are two districts with the same name in two different states(Ambiguity Issue). Or slight difference in the spellings in the data and that are present on the Indian map.

- There were around 18 such issues. To resolve this, I searched for the district name in the search bar of Tableau Map. Used Point Annotate to extract latitude and longitude. Then entered those values wherever there was such issue.

With these issue resolved, I moved on to making different plots and Dashboards. 

<h4> Dashboard 1 </h4>
- This dashboard contains States and Districts demarcations and also a webpage. I have included a hyperlink action in this dashboard. When clicked on any state or district, corresponding Wikipedia page opens in the web page  container.

<h4> Dashboard 2 </h4>
- This dashboard shows distribution of different measures related to Population and type of workers
  between states. I have used a parameter which is used to toggle between different measures. This paremeter has been used in a calculated field to return corresponding measure by the calculated filed.
  This calculated field is used to color the map I have also used Highlight Action in this dashboard. If a state is highlighted in one sheet then the corresponding state would also get highlighted in the other sheet.

<h4> Dashboard3 </h4>

- This dashboard shows the value of population measures and type of workers measures for the filtered state. The filter is applied across multiple sheets to change the value dynamically.

<h4> Sheet: Literate Statewise </h4>

- I have used measure names and measure values to create this sheet along with filter on measure names to show the bars only for Literacy related measures. I have also used state filter to compare between states.

<h4> Sheet: Religion% </h4>

- To create this bubble chart, I used measure values and measure names along with filter on
  measure names to plot the values related to Religion measures.