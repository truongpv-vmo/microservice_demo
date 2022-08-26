# microservice_demo
## Architecture
![image](https://user-images.githubusercontent.com/111956442/186799377-1fad395f-9f2c-475b-87b3-c2d10d200162.png)
<table>
    <tr>
        <td></td>
        <td>Tech</td>
        <td>description </td>
    </tr>
    <tr>
        <td>main api</td>
        <td>flask</td>
        <td>api login, get all product, recommendation </td>
    </tr>
    <tr>
        <td>cart</td>
        <td>fast api</td>
        <td>add products to cart </td>
    </tr>
    <tr>
        <td>recommendationservice</td>
        <td>grpc</td>
        <td>Recommends other products based on what's given in the cart.&nbsp; </td>
    </tr>
    <tr>
        <td>productcatalogservice</td>
        <td>grpc</td>
        <td>Provides the list of products&nbsp; </td>
    </tr>
 </table>
 
## authentication
![image](https://user-images.githubusercontent.com/111956442/186800034-c52e9b9f-50c4-4bed-b76a-9b3b6535c29b.png)
![image](https://user-images.githubusercontent.com/111956442/186800062-0f362b72-90fb-4b74-93b4-7b0a9caccbd8.png)
