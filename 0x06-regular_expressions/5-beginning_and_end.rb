#!/usr/bin/env ruby
# ^ matches the beginning of a line
# $ matches position at the end of a string
puts ARGV[0].scan(/^h.n$/).join
