def balanced(chars)
    count = 0
    for char in chars.each_char do 
        if char == '('
            count += 1
        elsif char == ')'
            count -= 1
        end
    end
    return count == 0
end


