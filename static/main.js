document.addEventListener('DOMContentLoaded', function() {
    // Navbar HTML
    const navbarHtml = `
    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid">
            <a class="navbar-brand text-light" href="#">SlateCMS</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse fw-bold" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item active">
                        <a class="nav-link text-dark" href="${window.location.origin}">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-light" href="${window.location.origin}/about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-light" href="${window.location.origin}/contact">Contact Us</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-light" href="${window.location.origin}/blogs">Blogs</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    `;

    // Footer HTML
    const footerHtml = `
    <footer class="text-light py-4 mt-5">
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <h5>Quick Links</h5>
                    <ul class="list-unstyled">
                        <li><a href="${window.location.origin}/" class="text-light">Home</a></li>
                        <li><a href="${window.location.origin}/about" class="text-light">About Us</a></li>
                        <li><a href="${window.location.origin}/contact" class="text-light">Contact Us</a></li>
                        <li><a href="${window.location.origin}/blogs" class="text-light">Blogs</a></li>
                    </ul>
                </div>
                <div class="col-md-4">
                    <h5>Legal</h5>
                    <ul class="list-unstyled">
                        <li><a href="${window.location.origin}/privacy-policy" class="text-light">Privacy Policy</a></li>
                        <li><a href="${window.location.origin}/terms-of-service" class="text-light">Terms of Service</a></li>
                    </ul>
                </div>
                <div class="col-md-4">
                    <h5>Contact Us</h5>
                    <p>Email: slatecms@gmail.com</p>
                    <p>Phone: +91 9232311212</p>
                    <p>Address: 82, Mansarovar, Jaipur, Rajasthan</p>
                </div>
            </div>
            <hr class="mt-4">
            <div class="row">
                <div class="col-md-6">
                    <p>&copy; 2025 SlateCMS. All rights reserved.</p>
                </div>
                <div class="col-md-6 text-md-end">
                    <a href="#" class="text-light me-3"><i class="fab fa-facebook-f"></i></a>
                    <a href="#" class="text-light me-3"><i class="fab fa-twitter"></i></a>
                    <a href="#" class="text-light me-3"><i class="fab fa-linkedin-in"></i></a>
                    <a href="#" class="text-light"><i class="fab fa-instagram"></i></a>
                </div>
            </div>
        </div>
    </footer>
    `;
    document.body.insertAdjacentHTML('afterbegin', navbarHtml);
    document.body.insertAdjacentHTML('beforeend', footerHtml);
});
