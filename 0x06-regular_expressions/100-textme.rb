#!/usr/bin/env ruby
# A regular expression that matches a given pattern
match_data = ARGV[0].match(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/)
puts "#{match_data[1]},#{match_data[2]},#{match_data[3]}" if match_data
