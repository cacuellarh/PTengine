from TrackMyPrice.Infraestructure.ServicesRegistration.InfraestructureServicesRegistration import InfraestructureServicesInject

def GetServicesApplications(injector) -> list:
    return [InfraestructureServicesInject]