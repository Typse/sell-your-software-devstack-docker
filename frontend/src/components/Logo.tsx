import styles from "./Logo.module.css"

const Logo = () => {
    return (
        <>
          <img src="src/assets/react.svg" alt="Sell your software logo" className={styles.logo} />
        </>
    );
};

export default Logo;
