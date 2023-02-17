import SourceCard from '../../components/SourceCard/SourceCard';
import styles from './SourcesPage.module.scss';

const sources = [
  {id: 1, name: 'Вышка', state: 'normal', rating: 4.92},
  {id: 2, name: 'МГТУ Баумана', state: 'critical', rating: 4.78},
  {id: 3, name: 'МФТИ', state: 'partial', rating: 4.95},
  {id: 4, name: 'Вышка', state: 'normal', rating: 4.92},
  {id: 5, name: 'МГТУ Баумана', state: 'critical', rating: 4.78},
  {id: 6, name: 'МФТИ', state: 'partial', rating: 4.95},
  {id: 7, name: 'Вышка', state: 'normal', rating: 4.92},
  {id: 8, name: 'МГТУ Баумана', state: 'critical', rating: 4.78},
  {id: 9, name: 'МФТИ', state: 'partial', rating: 4.95},
  {id: 10, name: 'МФТИ', state: 'partial', rating: 4.95},
]

const SourcesPage = () => {
  return (
    <div className={styles.container}>
      <h1 className='page_title'>Все ресурсы</h1>
      <div className={styles.table}>
        {sources.map((source, i) => <SourceCard i={i} key={source.id} {...source}/>)}
      </div>
    </div>
  );
};

export default SourcesPage;