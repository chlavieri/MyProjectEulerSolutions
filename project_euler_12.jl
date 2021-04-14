list_triangle_numbers = Int64[]

function triangle_numbers(n)
	i = 0
	while i <= n
		j = (i*(i+1))/2
		append!(list_triangle_numbers, j)
		i += 1
	end
	
	for j in list_triangle_numbers
		divisors = Int64[]
		for k in 1:j
			if j%k == 0
				append!(divisors, k)
			end
			if length(divisors) == 500
				println("The value of the number with over 500 divisors is ", j)
				break
			end
		end
	end
				
	
		
end
triangle_numbers(5000)
