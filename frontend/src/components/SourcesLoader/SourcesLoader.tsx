import React from 'react';
import ContentLoader from 'react-content-loader';

const SourcesLoader = () => {
  return (
    <ContentLoader 
      speed={2}
      width='100%'
      height='30rem'
      backgroundColor="#11152e"
      foregroundColor="#0E132F"
      style={{
        border: '1px solid rgb(40, 45, 69)',
        maxWidth: '74.5rem',
        minHeight: '30rem',
        marginTop: '.6rem',
        marginBottom: '.6rem',
        borderRadius: '.5rem'
      }}
    >
      <rect 
        width="100%" 
        height="100%" 
      /> 
    </ContentLoader>
  );
};

export default SourcesLoader;