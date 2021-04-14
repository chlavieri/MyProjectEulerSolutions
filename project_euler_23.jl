# project euler 23
abundant = []
cannot = []
can = []

for i in 2:28123
    divisors = []
    for j in 1:i
        if i%j == 0 && i != j
            append!(divisors, j)
        end
        if sum(divisors) > i
            append!(abundant, i)
        end
    end
end

for i in 2:28123
    for j in abundant
        for k in abundant
            if i == j+k
                append!(can, i)
            end
        end
    end
end
for i in 2:28123
    if i !in can
        append!(cannot, i)
    end
end

println("The sum of the numbers which cannot be written as the sum of two abundant numbers is", sum(cannot))