The given string has pipe delimited nodes that represent family members in a family tree. Each node is a CSV with the values being "parent_id, node_id, node_name".  Write a method that takes an input string and return a single result that represents the data as a hierarchy (root, children, siblings, etc).

Sample input: 

``null,0,grandpa|0,1,son|0,2,daugther|1,3,grandkid|1,4,grandkid|2,5,grandkid|5,6,greatgrandkid``