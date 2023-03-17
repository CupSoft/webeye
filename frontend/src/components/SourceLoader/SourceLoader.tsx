import React from 'react';
import ContentLoader from 'react-content-loader';

const SourceLoader = () => {
  return (
    <ContentLoader 
      speed={2}
      width='100%'
      height='37rem'
      backgroundColor="#11152F"
      foregroundColor="#2f364e"
      style={{
        border: '1px solid rgb(40, 45, 69)',
        maxWidth: '74.5rem',
        marginBottom: '1.2rem',
        marginTop: '5rem',
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

export default SourceLoader;