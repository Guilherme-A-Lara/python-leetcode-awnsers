'''
Dados dois arrays ordenados nums1 e nums2 de tamanho m e n respectivamente, 
retorne a mediana dos dois arrays ordenados. A complexidade geral do tempo de execução deve ser O(log (m n)).
'''

#Existem dois arrays ordenados nums1 e nums2 de tamanho m e n respectivamente.
#Encontra a mediana dos dois arrays ordenados.
#A complexidade geral do tempo de execução deve ser O(log (m+n)).
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    
    def findMedianSortedArrays(self, nums1, nums2):
        #A len()função retorna o número de itens em um objeto.
        m = len(nums1)
        n = len(nums2)
        if m > n :
            return self.findMedianSortedArrays(nums2, nums1)
        k = (m + n - 1) / 2
        l = 0
        #A min()função retorna o item com o valor mais baixo ou o item com o valor mais baixo em um iterável.
        r = min(m, k)
        
        #iniciar busca binária
        while l < r:
            midNums1 = (l + r) / 2
            midNums2 = k - midNums1
            if nums1[midNums1] < nums2[midNums2]:
                l += 1
            else:
                r = midNums1
        # após a busca binária, quase obtemos a mediana porque ela deve estar entre
        # estes 4 números: A[l-1], A[l], B[k-l] e B[k-l 1]
    
        # se (n+m) for ímpar, a mediana é a maior entre A[l-1] e B[k-l].
        # e há alguns casos de canto que precisamos cuidar.
        a = max(nums1[l-1] if l > 0  else float('-inf'), nums2[k-l] if k-l >= 0 else float('-inf'))
        if (m + n) & 1 == 1:
            return a
        b = min(nums1[l] if l < m else float('inf'), nums2[k-l+1] if k-l+1 < n else float('inf'))
        return (a+b)/2.0
      
'''
  Your input [1,3] [2]
  
  Output
  2.00000
  2.50000
  
  Expected
  2.00000
  2.50000
'''
