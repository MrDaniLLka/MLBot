clf = pickle.load(open(os.path.join('model.pkl'), 'rb'))
df = pd.read_csv('labeled.csv')

clf.fit(df['comment'], df[])
