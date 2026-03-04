from sklearn.preprocessing import StandardScaler


def limpar_dados(df):
    df = df.copy()
    df.drop(columns=["ID"], inplace=True)
    return df


def transformar_variaveis(df):
    df = df.copy()

    df['Sex'] = df['Sex'].map({0:'Male', 1:'Female'})
    df['Marital status'] = df['Marital status'].map({0:'Single', 1:'Non-single'})
    df['Education'] = df['Education'].map({
        0:'Other/Unknown',
        1:'High school',
        2:'University',
        3:'Graduate school'
    })
    df['Occupation'] = df['Occupation'].map({
        0:'Unemployed/Unskilled',
        1:'Skilled employee/Official',
        2:'Management/Highly qualified'
    })
    df['Settlement size'] = df['Settlement size'].map({
        0:'Small city',
        1:'Mid-sized city',
        2:'Big city'
    })

    return df


def padronizar_features(df, colunas):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[colunas])
    return X_scaled, scaler