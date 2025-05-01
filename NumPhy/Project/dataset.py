"""
| Order ID | Customer Age | Product Category | Product Price | Quantity | Discount (%) | Delivery Time (days) | Rating (out of 5) |
|----------|---------------|------------------|----------------|----------|----------------|------------------------|--------------------|
| 1001     | 28            | Electronics       | 249.99         | 1        | 5              | 3                      | 4.2                |
| 1002     | 35            | Clothing          | 39.99          | 2        | 0              | 5                      | 4.0                |
| 1003     | 22            | Books             | 12.49          | 3        | 10             | 2                      | 4.7                |
| 1004     | 31            | Electronics       | 499.99         | 1        | 15             | 4                      | 3.9                |
| 1005     | 45            | Home              | 89.99          | 1        | 0              | 6                      | 4.3                |
| ...      | ...           | ...               | ...            | ...      | ...            | ...                    | ...                |


"""
# total revenue

import numpy as np
revenue=np.array([249.99,39.99,12.49,499.99,89.99])
avg_revenue=np.mean(revenue)
quantity=np.array([1,2,3,1,1])
discount=np.array([5,0,10,15,0])
net_revenue= (revenue -(discount/100 *revenue) ) * quantity


print(avg_revenue)
print(net_revenue)