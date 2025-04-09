
var N = 0
var K = 0

if let input = readLine() {
    let nK = input.split(separator: " ").compactMap { Int($0) }
    if nK.count == 2 {
        N = nK[0]
        K = nK[1]
    }
}

// 2부터 N까지 배열 만들기
var numbers = Array(2...N)
var isRemoved = Array(repeating: false, count: N + 1)
var count = 0

for i in 2...N {
    if isRemoved[i] { continue } // 이미 지워진 수는 패스

    // i의 배수를 모두 지움
    for j in stride(from: i, through: N, by: i) {
        if !isRemoved[j] {
            isRemoved[j] = true
            count += 1
            if count == K {
                print(j)
                break
            }
        }
    }

    if count == K {
        break
    }
}
