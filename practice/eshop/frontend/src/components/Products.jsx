import axios from "axios";
import { useEffect, useState } from "react";

function Products() {

    const [products, setProducts] = useState([]);

    const [search, setSearch] = useState("");

    const [formData, setFormData] = useState({
        category: "",
        name: "",
        price: "",
        qty: ""
    });

    const [editId, setEditId] = useState(null);

    // Load Products
    const getProducts = () => {

        axios.get("http://127.0.0.1:8000/eshop/product")

        .then((response) => {

            setProducts(response.data.data);

        })

        .catch((error) => {

            console.log(error);

        });
    };

    useEffect(() => {

        getProducts();

    }, []);

    // Handle Input
    const handleChange = (e) => {

        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    // Add Product
    const addProduct = () => {

        const data = [{
            category: formData.category,
            name: formData.name,
            price: formData.price,
            qty: formData.qty
        }];

        axios.post(
            "http://127.0.0.1:8000/eshop/product",
            data
        )

        .then(() => {

            getProducts();

            setFormData({
                category: "",
                name: "",
                price: "",
                qty: ""
            });

        })

        .catch((error) => {

            console.log(error);

        });
    };

    // Delete Product
    const deleteProduct = (id) => {

        axios.delete(
            `http://127.0.0.1:8000/eshop/product/${id}`
        )

        .then(() => {

            getProducts();

        })

        .catch((error) => {

            console.log(error);

        });
    };

    // Edit Product
    const editProduct = (product) => {

        setEditId(product.id);

        setFormData({
            category: product.category,
            name: product.name,
            price: product.price,
            qty: product.qty
        });
    };

    // Update Product
    const updateProduct = () => {

        axios.put(
            `http://127.0.0.1:8000/eshop/product/${editId}`,
            formData
        )

        .then(() => {

            getProducts();

            setEditId(null);

            setFormData({
                category: "",
                name: "",
                price: "",
                qty: ""
            });

        })

        .catch((error) => {

            console.log(error);

        });
    };

    // Search
    const filteredProducts = products.filter((product) =>

        product.name.toLowerCase().includes(
            search.toLowerCase()
        )
    );

    return (

        <div className="container mt-5">

            <h1 className="text-center mb-4">
                Product CRUD
            </h1>

            {/* Search */}

            <input
                type="text"
                placeholder="Search Product"
                className="form-control mb-4"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
            />

            {/* Form */}

            <div className="card p-4 mb-5 shadow">

                <input
                    type="number"
                    name="category"
                    placeholder="Category ID"
                    className="form-control mb-3"
                    value={formData.category}
                    onChange={handleChange}
                />

                <input
                    type="text"
                    name="name"
                    placeholder="Product Name"
                    className="form-control mb-3"
                    value={formData.name}
                    onChange={handleChange}
                />

                <input
                    type="number"
                    name="price"
                    placeholder="Price"
                    className="form-control mb-3"
                    value={formData.price}
                    onChange={handleChange}
                />

                <input
                    type="number"
                    name="qty"
                    placeholder="Quantity"
                    className="form-control mb-3"
                    value={formData.qty}
                    onChange={handleChange}
                />

                {
                    editId ?

                    <button
                        className="btn btn-warning"
                        onClick={updateProduct}
                    >
                        Update Product
                    </button>

                    :

                    <button
                        className="btn btn-primary"
                        onClick={addProduct}
                    >
                        Add Product
                    </button>
                }

            </div>

            {/* Product List */}

            <div className="row">

                {
                    filteredProducts.map((product) => (

                        <div
                            className="col-md-4 mb-4"
                            key={product.id}
                        >

                            <div className="card p-3 shadow">

                                <h3>{product.name}</h3>

                                <p>
                                    Category : {product.category}
                                </p>

                                <p>
                                    Price : ₹{product.price}
                                </p>

                                <p>
                                    Qty : {product.qty}
                                </p>

                                <button
                                    className="btn btn-danger"
                                    onClick={() => deleteProduct(product.id)}
                                >
                                    Delete
                                </button>

                                <button
                                    className="btn btn-success mt-2"
                                    onClick={() => editProduct(product)}
                                >
                                    Edit
                                </button>

                            </div>

                        </div>
                    ))
                }

            </div>

        </div>
    );
}

export default Products;