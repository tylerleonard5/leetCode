

int maxArea(int* height, int heightSize){
    if(heightSize <= 1)
        return 0;
    
    
    if(heightSize == 2)
    {
        return ((height[0] < height[1]) ? height[0] : height[1]);
    }
    
    int front = 0;
    int back = heightSize-1;
    int max_area = 0;
    
    while(front < back){
         
        int current_area = (back - front) * ((height[back] <= height[front]) ? height[back] : height[front]);
        
        if(current_area > max_area)
            max_area = current_area;
        
        // Whichever height is smaller is the one restricting our max.
        // So, we look for a taller column to replace our smallest one.
        if(height[back] < height[front])
        {
            back--;
        } 
        else
        {
            front++;
        }
     }
     return max_area;
}

