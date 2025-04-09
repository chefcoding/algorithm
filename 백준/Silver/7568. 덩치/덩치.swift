let n = Int(readLine()!)!

var people:[(weight: Int, height: Int)] = []

for _ in 0..<n{
    if let input = readLine(){
        let parts = input.split(separator:" ").compactMap{Int($0)}
        if parts.count == 2{
            people.append((parts[0],parts[1]))
        }
    }
}

var ranks: [Int] = []

for i in 0..<n{
    var rank = 1
    
    for j in 0..<n {
        if i == j {continue}
        
        if people[j].weight > people[i].weight && people[j].height > people[i].height {
            rank += 1
        }
    }
    ranks.append(rank)
}

print(ranks.map {String($0)}.joined(separator:" "))




