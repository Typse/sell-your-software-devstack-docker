import { Link } from "react-router-dom";
import Logo from "./Logo"
import styles from "./Navbar.module.css"

const Navbar = () => {
  return (
      <nav className={styles.nav}>
        <Logo />
        <ul className={styles.navList}>
          <li><Link to="/shop">Shop</Link></li>
          <li><Link to="/admin">Admin</Link></li>
        </ul>
      </nav>
  );
};

export default Navbar;

