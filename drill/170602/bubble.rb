def swap(a, b)
    if a < b
        [a, b]
    else
        [b, a]
    end
end


def bubble(l)
    l.each_with_index {|v, i|
        l.slice(i, l.length).each_with_index {|value, index|
            a = l[index]
            b = l[index+1]
            if b != nil 
                a, b = swap(a, b)
                l[index] = a
                l[index+1] = b
            end
        }
    }
    l
end

p bubble([10,4,2,4,5,6])
