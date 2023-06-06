import cv2

def main():
    # Ouvrir la webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Lire une image de la webcam
        ret, frame = cap.read()

        # Afficher l'image
        cv2.imshow('Video', frame)

        # Attendre une touche
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Fermer la webcam
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
