import SourceCard from '../../components/SourceBadge/SourceBadge';
import { useGetAllSourcesMutation } from '../../services/apiService/apiService';
import styles from './SourcesPage.module.scss';

const sources = [
  {uuid: '1', name: 'Вышка', state: 'ok', rating: 4.92},
  {uuid: '2', name: 'МГТУ Баумана', state: 'critical', rating: 4.78},
  {uuid: '3', name: 'МФТИ', state: 'partial', rating: 4.95},
  {uuid: '4', name: 'Вышка', state: 'ok', rating: 4.92},
  {uuid: '5', name: 'МГТУ Баумана', state: 'critical', rating: 4.78},
  {uuid: '6', name: 'МФТИ', state: 'partial', rating: 4.95},
  {uuid: '7', name: 'Вышка', state: 'ok', rating: 4.92},
  {uuid: '8', name: 'МГТУ Баумана', state: 'critical', rating: 4.78},
  {uuid: '9', name: 'МФТИ', state: 'partial', rating: 4.95},
  {uuid: '10', name: 'МФТИ', state: 'partial', rating: 4.95},
]

const SourcesPage = () => {
  const [getAllSources, {isLoading, data}] = useGetAllSourcesMutation()

  // getAllSources().then(data => console.log(data))
  

  return (
    <div className={styles.container}>
      <h1 className='page_title'>Все ресурсы</h1>
      <div className={styles.table}>
        {sources.map((source, i) => <SourceCard i={i} key={source.uuid} {...source}/>)}
      </div>
    </div>
  );
};

export default SourcesPage;