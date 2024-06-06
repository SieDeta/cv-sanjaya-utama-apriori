import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from datetime import datetime
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# Fungsi untuk membaca file csv
def load_data(file):
    data = pd.read_csv(file)
    return data


def fill_missing_values(data):
    # Mengisi nilai kosong dengan nilai dari baris sebelumnya
    filled_data = data.fillna(method='ffill')
    return filled_data

# Fungsi untuk mengelompokkan nama barang (untuk visualisasi)
def group_barang(barang_name):
    if 'Strapping band' in barang_name:
        return 'Strapping band'
    if 'Strapping ban' in barang_name:
        return 'Strapping band'
    if 'SB' in barang_name:
        return 'Strapping band'
    if 'Sb' in barang_name:
        return 'Strapping band'
    elif 'Bubble' in barang_name:
        return 'Bubble'
    elif 'Pe' in barang_name:
        return 'Polietilena'
    elif 'pe' in barang_name:
        return 'Polietilena'
    elif 'SF' in barang_name:
        return 'SF'
    elif 'Siku' in barang_name:
        return 'Siku karet'
    elif 'Gripper' in barang_name:
        return 'Gripper'
    elif 'gripper' in barang_name:
        return 'Gripper'
    elif 'Foam sheet' in barang_name:
        return 'Foam sheet'
    elif 'Single face' in barang_name:
        return 'Single face'
    elif 'Styrofoam' in barang_name:
        return 'Styrofoam'
    elif 'Masking tape' in barang_name:
        return 'Masking tape'
    elif 'Foam sheet' in barang_name:
        return 'Foam sheet'
    elif 'Edge' in barang_name:
        return 'Edge Protector'
    elif 'PET' in barang_name:
        return 'PET'
    elif 'Pet' in barang_name:
        return 'PET'
    elif 'Servis' in barang_name:
        return 'Servis'
    elif 'servis' in barang_name:
        return 'Servis'
    elif 'Laker' in barang_name:
        return 'Laker/bearing'
    elif 'bearing' in barang_name:
        return 'Laker/bearing'
    elif 'Alat packing SB' in barang_name:
        return 'Alat packing SB'
    elif 'Slade' in barang_name:
        return 'Slade lidah'
    elif 'Gear' in barang_name:
        return 'Gear'
    elif 'Potenssio' in barang_name:
        return 'Potenssio'
    elif 'Bearing' in barang_name:
        return 'Laker/bearing'
    elif 'Gesper' in barang_name:
        return 'Gesper'
    elif 'spare part' in barang_name:
        return 'spare part'
    elif 'Klem' in barang_name:
        return 'Klem'
    elif 'Kawat' in barang_name:
        return 'Kawat'
    elif 'Lakban' in barang_name:
        return 'Lakban'
    elif 'Gum' in barang_name:
        return 'Gum Tape'
    elif 'Isolasi' in barang_name:
        return 'Isolasi'
    elif 'Plastik' in barang_name:
        return 'Plastik'
    elif 'Marking' in barang_name:
        return 'Marking'
    elif 'Las' in barang_name:
        return 'Las'
    elif 'V belt' in barang_name:
        return 'V belt'
    elif 'Baut' in barang_name:
        return 'Baut'
    elif 'Per' in barang_name:
        return 'Per'
    elif 'Rafia' in barang_name:
        return 'Rafia'
    elif 'Line' in barang_name:
        return 'Line'
    elif 'roler' in barang_name:
        return 'Roler'
    else:
        return barang_name

# Fungsi untuk mengelompokkan nama barang (untuk preprocessing)
def proces_group_barang(barang_name):
    if 'kuning' in barang_name:
        return 'Strapping band kuning'
    if 'biru' in barang_name:
        return 'Strapping band biru'
    if 'hijau' in barang_name:
        return 'Strapping band hijau'
    if 'hitam' in barang_name:
        return 'Strapping band hitam'
    if 'merah' in barang_name:
        return 'Strapping band merah'
    if 'putih' in barang_name:
        return 'Strapping band putih'
    elif 'Bubble' in barang_name:
        return 'Bubble'
    elif 'Pe' in barang_name:
        return 'Polietilena'
    elif 'pe' in barang_name:
        return 'Polietilena'
    elif 'SF' in barang_name:
        return 'SF'
    elif 'Siku' in barang_name:
        return 'Siku karet'
    elif 'Gripper' in barang_name:
        return 'Gripper'
    elif 'gripper' in barang_name:
        return 'Gripper'
    elif 'Foam sheet' in barang_name:
        return 'Foam sheet'
    elif 'Single face' in barang_name:
        return 'Single face'
    elif 'Styrofoam' in barang_name:
        return 'Styrofoam'
    elif 'Masking tape' in barang_name:
        return 'Masking tape'
    elif 'Foam sheet' in barang_name:
        return 'Foam sheet'
    elif 'Edge' in barang_name:
        return 'Edge Protector'
    elif 'PET' in barang_name:
        return 'PET'
    elif 'Pet' in barang_name:
        return 'PET'
    elif 'Servis' in barang_name:
        return 'Servis'
    elif 'servis' in barang_name:
        return 'Servis'
    elif 'Laker' in barang_name:
        return 'Laker/bearing'
    elif 'bearing' in barang_name:
        return 'Laker/bearing'
    elif 'Alat packing SB' in barang_name:
        return 'Alat packing SB'
    elif 'Slade' in barang_name:
        return 'Slade lidah'
    elif 'Gear' in barang_name:
        return 'Gear'
    elif 'Potenssio' in barang_name:
        return 'Potenssio'
    elif 'Bearing' in barang_name:
        return 'Laker/bearing'
    elif 'Gesper' in barang_name:
        return 'Gesper'
    elif 'spare part' in barang_name:
        return 'spare part'
    elif 'Klem' in barang_name:
        return 'Klem'
    elif 'Kawat' in barang_name:
        return 'Kawat'
    elif 'Lakban' in barang_name:
        return 'Lakban'
    elif 'Gum' in barang_name:
        return 'Gum Tape'
    elif 'Isolasi' in barang_name:
        return 'Isolasi'
    elif 'Plastik' in barang_name:
        return 'Plastik'
    elif 'Marking' in barang_name:
        return 'Marking'
    elif 'Las' in barang_name:
        return 'Las'
    elif 'V belt' in barang_name:
        return 'V belt'
    elif 'Baut' in barang_name:
        return 'Baut'
    elif 'Per' in barang_name:
        return 'Per'
    elif 'Rafia' in barang_name:
        return 'Rafia'
    elif 'Line' in barang_name:
        return 'Line'
    elif 'roler' in barang_name:
        return 'Roler'
    else:
        return barang_name

# Fungsi untuk memfilder data csv berdasarkan tanggal
def filter_data_by_date_range(data, date_column, start_date, end_date):
    # Konversi kolom tanggal dalam DataFrame menjadi objek datetime.date
    data[date_column] = pd.to_datetime(
        data[date_column], errors='coerce').dt.date

    # Lakukan filter dengan perbandingan antara datetime.date
    filtered_data = data[(data[date_column] >= start_date)
                         & (data[date_column] <= end_date)]
    filtered_data['Grouped_BARANG'] = filtered_data['BARANG'].apply(
        group_barang)
    filtered_data['Proces_Group_BARANG'] = filtered_data['BARANG'].apply(
        proces_group_barang)
    return filtered_data


def preprocess_data(data):
    # Menghitung jumlah kemunculan DEBIT dan TANGGAL
    debit_date_counts = data.groupby(
        ['DEBIT', 'TGL']).size().reset_index(name='count')

    # Memilih DEBIT yang memiliki lebih dari 1 entri unik dengan TANGGAL yang berbeda
    valid_debits = debit_date_counts['DEBIT'][debit_date_counts.groupby(
        'DEBIT')['TGL'].transform('nunique') > 1].unique()

    # Filter data berdasarkan DEBIT dan TANGGAL yang valid
    filtered_data = data[data['DEBIT'].isin(valid_debits)]

    # Melakukan pengelompokan hanya berdasarkan 'DEBIT' dan 'BARANG'
    transaksiSJY = (filtered_data.groupby(['DEBIT', 'Proces_Group_BARANG'])
                    .size().unstack().reset_index().fillna(0)
                    .set_index('DEBIT'))

    st.write(filtered_data)
    
    transaksiSJY = transaksiSJY.apply(pd.to_numeric, errors='coerce') # Mengubah jadi nilai numerik
    transaksiSJYEncoded = transaksiSJY.applymap(lambda x: 1 if x >= 1 else 0) # Jika nilai > 1 = 1, jika 0 = 0
    transaksiSJY = transaksiSJYEncoded
    transaksiSJY.fillna(0, inplace=True) # Mengganti semua nilai NaN dengan 0

    return transaksiSJY


def plot_data_preprocessing(filtered_data):
    # Mengonversi kolom TGL menjadi tipe data datetime
    filtered_data['TGL'] = pd.to_datetime(
        filtered_data['TGL'], format='%d/%m/%Y')

    # Mengonversi kolom QTY ke tipe data numerik dan mengganti NaN dengan 0
    filtered_data[' QTY '] = pd.to_numeric(
        filtered_data[' QTY '], errors='coerce').fillna(0)

    # Membuat kolom baru 'Bulan' untuk menyimpan informasi bulan dari tanggal transaksi
    filtered_data['Bulan'] = filtered_data['TGL'].dt.to_period('M')

    # Menghitung total penjualan (QTY) per bulan
    sales_per_month = filtered_data.groupby('Bulan')[' QTY '].sum()

    # Visualisasi line chart untuk total penjualan per bulan
    st.subheader(
        'Total Penjualan Barang per Bulan')
    plt.figure(figsize=(10, 6))
    sales_per_month.plot(kind='line', marker='o', linestyle='-')
    plt.xlabel('Bulan')
    plt.ylabel('Total Penjualan')
    # plt.title('Total Penjualan Barang per Bulan')
    st.pyplot(plt)

    # Visualisasi bar chart untuk jumlah transaksi per BARANG (hanya 10 data teratas)
    st.subheader('Total Transaksi per BARANG')
    plt.figure(figsize=(8, 6))
    filtered_data['Grouped_BARANG'].value_counts().nlargest(
        10).plot(kind='bar')
    plt.xlabel('Barang')
    plt.ylabel('Jumlah Transaksi')
    plt.title('Top 10')
    st.pyplot(plt)

    # Menghitung jumlah barang yang ditransaksikan per DEBIT
    barang_per_debit = filtered_data.groupby(
        'DEBIT')['BARANG'].nunique().sort_values(ascending=False)

    # Visualisasi bar chart untuk jumlah barang yang ditransaksikan per DEBIT (hanya 10 data teratas)
    st.subheader('Jumlah Barang yang Ditransaksikan per DEBIT')
    plt.figure(figsize=(10, 6))
    barang_per_debit.head(15).plot(kind='bar')
    plt.xlabel('DEBIT')
    plt.ylabel('Jumlah Barang yang Ditransaksikan')
    plt.title('Top 10')
    st.pyplot(plt)

    # Visualisasi pie chart untuk jumlah transaksi per BARANG (hanya 10 data teratas)
    st.subheader('Persentase Transaksi per BARANG')
    plt.figure(figsize=(8, 6))
    filtered_data['Grouped_BARANG'].value_counts().nlargest(
        10).plot(kind='pie', autopct='%1.1f%%')
    plt.title('Top 10')
    st.pyplot(plt)


def main():
    st.title('Aplikasi Data Mining')

    # Menyimpan variabel data di session state
    if 'data' not in st.session_state:
        st.session_state.data = None

    # Menyimpan variabel filtered_data di session state
    if 'filtered_data' not in st.session_state:
        st.session_state.filtered_data = None

    # Menyimpan variabel rules di session state
    if 'rules' not in st.session_state:
        st.session_state.rules = None

    # Navbar Horizontal Menu
    selected = option_menu(None, ["Home", "Filter", "Visualisasi", 'Hasil'], 
        icons=['house', 'funnel', "bar-chart", 'check2-square'], 
        menu_icon="cast", default_index=0, orientation="horizontal")

    # ==== HOME =======
    if selected == "Home":
        # File upload
        uploaded_file = st.file_uploader("Upload file CSV", type=['csv'])

        if uploaded_file is not None:
            st.session_state.data = load_data(uploaded_file)
            st.session_state.data = fill_missing_values(st.session_state.data)

        st.subheader('Pratinjau Data')
        st.write(st.session_state.data)
    # ===== END OF HOME ===

    # ======= Filter =======
    if selected == "Filter":
        if st.session_state.data is not None:
            data = st.session_state.data
            # Filter Range Tanggal
            min_date = pd.to_datetime(data['TGL'], errors='coerce').min()
            max_date = pd.to_datetime(data['TGL'], errors='coerce').max()

            start_date = st.date_input(
                "Tanggal Awal", min_value=min_date, max_value=max_date, value=min_date)
            end_date = st.date_input(
                "Tanggal Akhir", min_value=min_date, max_value=max_date, value=max_date)

            if start_date <= end_date:
                filtered_data = filter_data_by_date_range(
                    data, 'TGL', start_date, end_date)

                st.subheader('Data Setelah Difilter')
                st.write(filtered_data)

                st.session_state.filtered_data = filtered_data

                # Masuk ke fungsi preprocess_data untuk merubah data menjadi binary 0 dan 1
                preprocessed_data = preprocess_data(filtered_data)

                # User input untuk minimum support, confidence, lift
                min_support = st.slider(
                    "Minimum Support", min_value=0.1, max_value=1.0, step=0.01, value=0.12)
                min_confidence = st.slider(
                    "Minimum Confidence", min_value=0.1, max_value=1.0, step=0.01, value=0.5)
                min_lift = st.slider(
                    "Minimum Lift", min_value=0.1, max_value=2.0, step=0.1, value=1.1)

                # Run Apriori algorithm berdasarkan user input
                frq_items = apriori(preprocessed_data,
                                    min_support=min_support, use_colnames=True)

                # Kumpulkan aturan yang disimpulkan ke dalam data frame
                rules = association_rules(
                    frq_items, metric="lift", min_threshold=min_confidence)
                rules = rules.sort_values(
                    ['confidence', 'lift'], ascending=[False, False])

                # Filter rules berdasarkan minimum lift
                rules = association_rules(
                    frq_items, metric="lift", min_threshold=min_lift)

                # Sort rules by confidence dan lift dalam urutan menurun
                rules = rules.sort_values(
                    ['confidence', 'lift'], ascending=[False, False])

                # Ubah setiap itemset menjadi list
                frq_items['itemsets'] = frq_items['itemsets'].apply(
                    lambda x: list(x))
                rules['antecedents'] = rules['antecedents'].apply(
                    lambda x: list(x))
                rules['consequents'] = rules['consequents'].apply(
                    lambda x: list(x))

                st.subheader('Frequent Itemsets')
                st.write(frq_items)

                st.subheader('Association Rules')
                st.write(rules)

                # Hasil rules disimpan di session state
                st.session_state.rules = rules

            else:
                st.error(
                    "Start Date should be before End Date. Please select a valid date range.")
        else:
            st.write("Silakan unggah file CSV terlebih dahulu di halaman Home.")
    # ===== END OF FILTER =============

    # ========= VISUALISASI =======
    if selected == "Visualisasi":
        if st.session_state.filtered_data is not None:  # Pastikan filtered_data sudah ada
            filtered_data = st.session_state.filtered_data
            plot_data_preprocessing(filtered_data)
        else:
            st.write("Silakan unggah file CSV terlebih dahulu di halaman Home.")
    #  END OF VISUALISASI ============

    # ======== HASIL =============
    if selected == "Hasil":
        if st.session_state.rules is not None:
            rules = st.session_state.rules
            st.subheader('Pola Transaksi')
            if not rules.empty:
                st.write("Hasil Pola Transaksi Pelanggan:")
                sorted_rules_recommendation = rules.sort_values(
                    ['confidence', 'lift'], ascending=[False, False]).reset_index(drop=True)
                for index, row in sorted_rules_recommendation.iterrows():
                    antecedents = row['antecedents']
                    consequents = row['consequents']

                    # Membuat teks rekomendasi dengan nama barang dalam bentuk bold
                    antecedents_str = ', '.join(
                        f"<strong>{item}</strong>" for item in antecedents)
                    consequents_str = ', '.join(
                        f"<strong>{item}</strong>" for item in consequents)

                    recommendation_text = f"{index + 1}. Jika pelanggan membeli {antecedents_str} , maka biasanya membeli {consequents_str}."
                    st.markdown(recommendation_text, unsafe_allow_html=True)
            else:
                st.write(
                    "Tidak ada rekomendasi yang dihasilkan dengan parameter yang diberikan.")

            st.subheader('Hasil Rekomendasi')
            if not rules.empty:
                st.write("Katalog promo untuk menaikkan pendapatan perusahaan:")

                seen_pairs = set()  # Inisialisasi set untuk melacak pasangan barang yang telah dilihat

                sorted_rules_knowledge = rules.sort_values(['confidence', 'lift'], ascending=[
                                                        False, False]).reset_index(drop=True)
                for index, row in sorted_rules_knowledge.iterrows():
                    antecedents = row['antecedents']
                    consequents = row['consequents']

                    # Urutkan pasangan barang untuk memudahkan pengecekan
                    pair = tuple(sorted([tuple(antecedents), tuple(consequents)]))

                    # Check jika pasangan barang sudah pernah ditampilkan sebelumnya
                    if pair not in seen_pairs:
                        antecedents_str = ', '.join(
                            f"<strong>{item}</strong>" for item in antecedents)
                        consequents_str = ', '.join(
                            f"<strong>{item}</strong>" for item in consequents)

                        knowledge_text = f"{len(seen_pairs) + 1}. Membuat promo menggunakan pasangan barang {antecedents_str} dengan barang {consequents_str}."
                        st.markdown(knowledge_text, unsafe_allow_html=True)

                        # Tambahkan pasangan barang yang sudah ditampilkan ke dalam set seen_pairs
                        seen_pairs.add(pair)
            else:
                st.write(
                    "Tidak ada rekomendasi yang dihasilkan dengan parameter yang diberikan.")
        else:
            st.write("Silakan unggah file CSV terlebih dahulu di halaman Home.")
    # =========END OF HASIL =================


if __name__ == '__main__':
    main()
