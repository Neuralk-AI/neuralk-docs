import React from 'react';
import TOC from '@theme-original/TOC';

export default function TOCWrapper(props) {
  return (
    <>
      <p className="onthispage"> On this page</p>
      <TOC {...props} />
    </>
  );
}
// export default function TOCWrapper(props) {
//   return (
//     <>
//       <TOC {...props} />
//     </>
//   );
// }
