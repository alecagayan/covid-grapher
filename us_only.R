library(RCurl)
library(ggplot2)
library(scales) # to access break formatting functions

# download the data
fileStates <- getURL('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
fileCounties <- getURL('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv', ssl.verifyhost=FALSE, ssl.verifypeer=FALSE)

# import the data
dataStates <- read.csv(textConnection(fileStates), header=T)
dataCounties <- read.csv(textConnection(fileCounties), header=T)

# format the date field
dataStates$date <- as.Date(dataStates$date , format = "%Y-%m-%d")
dataCounties$date <- as.Date(dataCounties$date , format = "%Y-%m-%d")

# print top rows
head(dataStates)
head(dataCounties)

# aggregate cases and deaths by date
casesByDate <- aggregate(dataStates$cases, by=list(date=dataStates$date), FUN=sum)
deathsByDate <- aggregate(dataStates$deaths, by=list(date=dataStates$date), FUN=sum)

head(casesByDate)
head(deathsByDate)


# VA data
dataStatesVA <- dataStates[dataStates$state == 'Virginia',]
dataCountiesVA <- dataCounties[dataCounties$state == 'Virginia',]

casesByDateVA <- aggregate(dataStatesVA$cases, by=list(date=dataStatesVA$date), FUN=sum)
deathsByDateVA <- aggregate(dataStatesVA$deaths, by=list(date=dataStatesVA$date), FUN=sum)

head(casesByDateVA)
head(deathsByDateVA)

ggplot(data = casesByDate, aes(x = date, y = x)) +
  geom_point() +
  geom_point(data = deathsByDate, colour='red') +
  #geom_point(data = casesByDateVA, colour='blue') +
  #geom_point(data = deathsByDateVA, colour='purple') +
  labs(x = "Date",
       y = "New Cases",
       title = "US Cases by Date",
       subtitle = "Across 50 states") +
#  scale_x_date(breaks = function(x) seq.Date(from = min(x), 
#                                             to = max(x), 
#                                             by = "7 days")) +
  scale_y_log10(breaks = trans_breaks("log10", function(x) 10^x),
                labels = trans_format("log10", math_format(10^.x))) +
  theme_bw()
