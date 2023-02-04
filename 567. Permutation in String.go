func checkInclusion(s1 string, s2 string) bool {
	originHash := makeHash(s1)
	localHash := map[rune]int{}
	queue := []rune{}

	for _, latest := range s2 {
		localHash[latest] += 1
		queue = append(queue, latest)

		if compareHashs(originHash, localHash) {
			return true
		}
		if len(queue) == len(s1) {
			tar := queue[0]
			queue = queue[1:]
			localHash[tar] -= 1
		}
	}
	return false
}
func makeHash(s string) map[rune]int {
	ret := map[rune]int{}

	for _, c := range s {
		ret[c] += 1
	}
	return ret
}

func compareHashs(m1, m2 map[rune]int) bool {
	for k, v := range m1 {
		cnt, ok := m2[k]
		if !ok || cnt < v {
			return false
		}
	}
	return true
}