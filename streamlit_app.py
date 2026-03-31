<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jazan PMO - Project Management Office</title>
    <!-- Bootstrap 5 CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- FontAwesome Icons CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts: Inter for English, Cairo for Arabic -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Cairo:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-theme sticky-top">
        <div class="container">
            <!-- Logo: Replace 'logo.png' with your actual logo file path. Adjust height as needed -->
            <a class="navbar-brand fw-bold" href="#home">
                <img src="logo.png" alt="" height="100" class="me-2">
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#home" data-en="Home" data-ar="الرئيسية">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#mission" data-en="Mission" data-ar="الرسالة">Mission</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#vision" data-en="Vision" data-ar="الرؤية">Vision</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#goals" data-en="Goals" data-ar="الأهداف">Goals</a>
                    </li>
                </ul>
                <!-- Language Toggle Button -->
                <button class="btn btn-outline-light ms-3" id="lang-toggle" data-lang="en">
                    <span id="lang-text">EN</span> / AR
                </button>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero-section d-flex align-items-center">
        <div class="container text-center text-white">
            <h1 class="display-4 fw-bold mb-3" data-en="Driving Excellence in Project Management" data-ar="قيادة التميز في إدارة المشاريع بأمانة منطقة جازان ">
                Driving Excellence in Project Management
            </h1>
            <p class="lead mb-4" data-en="Delivering strategic value and operational success in Jazan." data-ar="القيمة الاستراتيجية والنجاح التشغيلي للمشاريع">
                Delivering strategic value and operational success in Jazan.
            </p>
            <!-- CTA Button: Update href later -->
            <a href="https://app.powerbi.com/view?r=eyJrIjoiYjcwZTQ1ZTUtOTFmOC00Y2M4LWFkYzctY2FkNThkYjM5YzkwIiwidCI6Ijk4YWZlMGM0LTlkMzAtNDFjNy04Zjc0LTg2ODQxY2I0NTc1ZiIsImMiOjl9" class="btn btn-light btn-lg fw-bold" data-en="Go to Dashboard" data-ar="لوحة قياس أداء المشاريع">
                Go to Dashboard
            </a>
        </div>
    </section>

    <!-- About PMO Section -->
    <section class="about-section py-5">
        <div class="container">
            <div class="row g-4">
                <!-- Mission -->
                <div class="col-lg-4 col-md-6" id="mission">
                    <div class="card h-100 border-0 shadow-sm">
                        <div class="card-body text-center">
                            <i class="fas fa-bullseye fa-3x text-theme mb-3"></i>
                            <h5 class="card-title fw-bold" data-en="Our Mission" data-ar="رسالتنا">Our Mission</h5>
                            <p class="card-text" data-en="To execute projects efficiently and effectively, ensuring optimal resource utilization and stakeholder satisfaction." data-ar="تمكين أمانة منطقة جازان من إدارة مشاريعها بفعالية واحترافية، عبر توحيد المنهجيات، وتعزيز الحوكمة، وتقديم الدعم الفني والاستشاري، بما يضمن تحقيق الأهداف الاستراتيجية بكفاءة وجودة عالية  ">
                                To execute projects efficiently and effectively, ensuring optimal resource utilization and stakeholder satisfaction.
                            </p>
                        </div>
                    </div>
                </div>
                <!-- Vision -->
                <div class="col-lg-4 col-md-6" id="vision">
                    <div class="card h-100 border-0 shadow-sm">
                        <div class="card-body text-center">
                            <i class="fas fa-eye fa-3x text-theme mb-3"></i>
                            <h5 class="card-title fw-bold" data-en="Our Vision" data-ar="رؤيتنا">Our Vision</h5>
                            <p class="card-text" data-en="To become the leading Project Management Office in the region, setting benchmarks for excellence and innovation." data-ar="  أن يكون مكتب إدارة المشاريع ممكنًا رئيسيًا لتحقيق التميز المؤسسي، من خلال قيادة وتنظيم وتنفيذ المشاريع بكفاءة عالية وفق أفضل الممارسات العالمية، بما يدعم تحقيق مستهدفات التنمية المستدامة ورؤية المملكة  ">
                                To become the leading Project Management Office in the region, setting benchmarks for excellence and innovation.
                            </p>
                        </div>
                    </div>
                </div>
                <!-- Goals -->
                <div class="col-lg-4 col-md-12" id="goals">
                    <div class="card h-100 border-0 shadow-sm">
                        <div class="card-body text-center">
                            <i class="fa-solid fa-list-check fa-3x text-theme mb-3"></i>
                            <h5 class="card-title fw-bold" data-en="Our Goals" data-ar="أهدافنا">Our Goals</h5>
                            <ul id="goals-list" class="text-start" data-en="Standardize project management processes across all initiatives.|Enhance transparency and accountability in project execution.|Ensure timely delivery of projects within budget constraints.|Foster innovation and continuous improvement in project methodologies." data-ar="دعم التحول الرقمي في إدارة ومتابعة المشاريع.|دعم اتخاذ القرار من خلال التقارير ولوحات المعلومات المبنية على البيانات.|تعزيز الحوكمة والشفافية في إدارة المشاريع.|توحيد وتطبيق منهجيات إدارة المشاريع على مستوى الأمانة">
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-white py-4">
        <div class="container text-center">
            <p class="mb-3" data-en="© 2026 Jazan PMO " data-ar="© 2026 مكتب إدارة المشاريع بأمانة جازان ">
                © 2026 Jazan PMO. All rights reserved.
            </p>
            <div class="social-icons">
                <!-- Add actual links later -->
                <a href="#" class="text-white me-3" aria-label="Email"><i class="fas fa-envelope fa-lg"></i></a>
                <a href="#" class="text-white me-3" aria-label="Phone"><i class="fas fa-phone fa-lg"></i></a>
                <a href="#" class="text-white" aria-label="LinkedIn"><i class="fab fa-linkedin fa-lg"></i></a>
            </div>
        </div>
    </footer>

    <!-- Bootstrap JS CDN -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Custom JS -->
    <script src="script.js"></script>
</body>
</html>
