blood_type = ['O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+']

def get_blood_compatibility():
    while True:
        donor_blood_type = input("What is donor's blood type?: ").upper()
        receiver_blood_type = input("What is receiver's blood type?: ").upper()

        if donor_blood_type not in blood_type or receiver_blood_type not in blood_type:
            print("Invalid blood type. O-, O+, A-, A+, B-, B+, AB-, AB+ are the only blood types available.")
        else:
            break

    compatibility = False

    if donor_blood_type == 'O-':
        compatibility = True
    elif donor_blood_type == 'O+':
        if receiver_blood_type in ['O+', 'A+', 'B+', 'AB+']:
            compatibility = True
    elif donor_blood_type == 'A-':
        if receiver_blood_type in ['A-', 'A+', 'AB-', 'AB+']:
            compatibility = True
    elif donor_blood_type == 'A+':
        if receiver_blood_type in ['A+', 'AB+']:
            compatibility = True
    elif donor_blood_type == 'B-':
        if receiver_blood_type in ['B-', 'B+', 'AB-', 'AB+']:
            compatibility = True
    elif donor_blood_type == 'B+':
        if receiver_blood_type in ['B+', 'AB+']:
            compatibility = True
    elif donor_blood_type == 'AB-':
        if receiver_blood_type in ['AB-', 'AB+']:
            compatibility = True
    elif donor_blood_type == 'AB+':
        if receiver_blood_type in ['AB+']:
            compatibility = True

    if compatibility:
        print("Donor is compatible with receiver.")
    else:
        print("Donor is not compatible with receiver. Dangerous immunological reaction may occur if transfusion takes place.")

get_blood_compatibility()

disclaimer = "This script is for educational purposes only and clinical correlation is required!"
print(disclaimer)
