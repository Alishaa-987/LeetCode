class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        
        def search(l, r):
            if l > r: return False
            
            # solution to part 1
            # --- start ---
            m = (l + r) // 2
            orig_l, orig_r = l, r
            
            if target == nums[m]:
                return True
            
            if nums[l] <= nums[m] <= r:
                if target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[l] > nums[m]:
                    if nums[m] <= target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if nums[l] <= target <= nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
            # --- end ---
            
            # look at other part if we don't find it
            if not search(l,r):
                # search(l, m-1) failed, try search(m+1,r)
                if orig_l == l and not search(m + 1, orig_r):
                    return False
                # search(m+1,r) failed, try search(l, m-1)
                elif orig_r == r and not search(orig_l, m - 1):
                    return False
                
            return True
                
        return search(l,r)
		