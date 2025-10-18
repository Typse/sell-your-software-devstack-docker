import { useNavigate } from "react-router-dom";
import { useProducts } from "../context/ProductContext";

import styles from "./Shop.module.css"

const Shop = () => {
  const { products, loading } = useProducts();

  const navigate = useNavigate();

  const handleInspectProduct = (product_id: string) => {
    navigate(`/shop/${product_id}`);
  };

  if (loading) return <p>Lade Produkte...</p>;

  return (
    <>
      <h2>Shop</h2>
        {products.map((product) => (
          <div className={styles.productDiv}>
            <h3>{product.product_name}</h3>
            <img src="https://i.imgur.com/EHyR2nP.png" alt="Product picture" width={100}/>
            <p>{product.product_price} €</p>
            <button onClick={() => handleInspectProduct(product.product_id)}>Ansehen</button>
          </div>
        ))}
    </>
  );
};

export default Shop;
