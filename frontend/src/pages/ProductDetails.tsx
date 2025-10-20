import { useParams, useNavigate } from "react-router-dom";
import { useProducts } from "../context/ProductContext";

const ProductDetails = () => {
    const { productId } = useParams();
    const { products } = useProducts();
    const navigate = useNavigate();

    const product = products.find((p) => p.product_id === productId);

    if (!product) {
        return <p>Produkt nicht gefunden.</p>;
    }

    const handleCheckoutPress = () => {
        console.log("Gar kein Bock das zu machen...")
    };

    return (
        <>
            <h2>{product.product_name}</h2>
            <img
                src="https://i.imgur.com/EHyR2nP.png"
                alt={product.product_name}
                width={200}
            />
            <p>Preis: {product.product_price} €</p>
            {/* Anscheinend ist hier noch was falsch. product.product_description scheint 'None' zu sein.*/}
            <p>{product.product_description || "Keine Beschreibung verfügbar."}</p>

            <button onClick={handleCheckoutPress}>Jetzt kaufen</button>
            <button onClick={() => navigate(-1)}>Zurück</button>
        </>
    );
}

export default ProductDetails;
