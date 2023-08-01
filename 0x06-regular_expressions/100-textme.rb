#!/usr/bin/env ruby
matches = ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

if matches.any?
  sender = matches[0][0]
  receiver = matches[0][1]
  flags = matches[0][2]

  puts [sender, receiver, flags].join(",")

end
