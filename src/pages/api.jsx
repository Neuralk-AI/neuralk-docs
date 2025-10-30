import React from 'react';
import Layout from '@theme/Layout';

export default function ApiDocsPage() {
  return (
    <Layout title="API Docs" description="Neuralk SDK Python API Documentation">
      <div style={{ width: '100%', height: '100vh', border: 'none' }}>
        <iframe
          src="/sphinx-docs/index.html"
          title="Sphinx API Docs"
          style={{
            width: '100%',
            height: '100%',
            border: 'none',
          }}
        />
      </div>
    </Layout>
  );
}



// / import React from 'react';
// import Layout from '@theme/Layout';
// import { RedocStandalone } from 'redoc';

// export default function ApiPage() {
//   return (
//     <Layout
//       title="API Docs"
//       description="Neuralk API Documentation">
//       <div style={{ width: '100%', minHeight: '100vh' }}>
//         <RedocStandalone
//           specUrl="/openapi.json" // Path to your OpenAPI JSON
//           options={{
//             theme: {
//               colors: { primary: { main: '#0d6efd' } },
//             },
//             scrollYOffset: () => {
//               // Adjust for Docusaurus navbar height
//               const navbar = document.querySelector('.navbar');
//               return navbar ? navbar.offsetHeight : 0;
//             },
//           }}
//         />
//       </div>
//     </Layout>
//   );
// }
