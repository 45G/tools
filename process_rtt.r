library(ggplot2)

data <- read.table("data64.txt", header=T, sep=" ")
df <- data[,c("Time", "BytesTitle", "Bytes", "RTTTitle", "RTT")]

p <- ggplot(data=df, aes(df$RTT))
p <- p + geom_histogram(breaks=seq(0, 215, by =5), aes(fill=..count..))
p <- p + scale_fill_gradient("Count", low = "red", high = "green")
p <- p + labs(x="RTT", y="Count")
p <- p + scale_x_continuous(breaks=seq(0,215,5))

ggsave("data64.pdf", width=15, height=5)
