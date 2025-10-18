import { createContext, useEffect, useState, ReactNode, useContext } from "react";

type Product = {
  product_id: string;
  price_id: string;
  product_name: string;
  product_description: string;
  product_price: number;
};

type ProductContextType = {
  products: Product[];
  loading: boolean;
};

const ProductContext = createContext<ProductContextType>({
  products: [],
  loading: true,
});

export const ProductProvider = ({ children }: { children: ReactNode }) => {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/products")
      .then((res) => res.json())
      .then((data) => setProducts(data))
      .catch((err) => console.error("Fehler beim Laden der Produkte:", err))
      .finally(() => setLoading(false));
  }, []);

  return (
    <ProductContext.Provider value={{ products, loading }}>
      {children}
    </ProductContext.Provider>
  );
};

export const useProducts = () => useContext(ProductContext);
