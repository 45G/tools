#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

library(ggplot2)

if (length(args)<3) {
  stop("Two arguments must be supplied (input_file output_file max).\n", call.=FALSE)
}


data <- read.table(args[1], header=T, sep=" ")
df <- data[,c("Time", "BytesTitle", "Bytes", "RTTTitle", "RTT")]

p <- ggplot(data=df, aes(df$RTT))
p <- p + geom_histogram(breaks=seq(0, as.integer(args[3]), by =5), aes(fill=..count..))
p <- p + scale_fill_gradient("Count", low = "red", high = "green")
p <- p + labs(x="RTT (ms)", y="Count")
p <- p + scale_x_continuous(breaks=seq(0,as.integer(args[3]),5))

ggsave(args[2], width=15, height=5)
